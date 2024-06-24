class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        t = []
        c = 0
        while(len(grid[0])!= 0):
            t = []
            for x in grid:
                t.append(max(x))
                x.remove(max(x))
            c += max(t)
        return c
