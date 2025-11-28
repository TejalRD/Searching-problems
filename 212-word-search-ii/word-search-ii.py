from typing import List, Dict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build Trie
        trie = {}
        END = "*"  # special key to mark end of word
        
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[END] = word  # store the full word at the end node
        
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r: int, c: int, node: Dict):
            ch = board[r][c]
            if ch not in node:
                return  # not a prefix -> prune
            
            next_node = node[ch]
            
            # 2. Check if we completed a word
            if END in next_node:
                result.append(next_node[END])
                # Remove it so we don’t add duplicates
                del next_node[END]
            
            # 3. Mark this cell as visited
            board[r][c] = "#"  # any placeholder not a lowercase letter
            
            # 4. Explore neighbors (up, down, left, right)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            
            # 5. Restore the cell (backtrack)
            board[r][c] = ch
            
            # 6. Optional: prune the trie node if it's now empty
            if not next_node:  # {} is falsy
                del node[ch]
        
        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        
        return result
