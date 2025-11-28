class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            
            if r<0 or r>=rows or c<0 or c>= cols:
                return False
            if board[r][c] != word[idx]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))

            board[r][c] = temp

            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False

        