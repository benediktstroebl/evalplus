
def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    #     int R = grid.length;
    #     int C = grid[0].length;
    #     int[][] M = new int[R][C];
    #     for (int r = 0; r < R; ++r) {
    #         for (int c = 0; c < C; ++c) {
    #             M[r][c] = grid[r][c] - 1;
    #         }
    #     }
    #     return min_path(M, 0, 0, new boolean[R][C], k);

    #     public List<Integer> min_path(int[][] M, int r, int c, boolean[][] used, int k) {
    #         List<Integer> result = new ArrayList<Integer>();
    #         if (k == 0) return result;

    #         used[r][c] = true;
    #         if (k == 1) {
    #             result.add(M[r][c] + 1);
    #             return result;
    #         }

    #         int[] dr = new int[]{-1, 0, 1, 0};
    #         int[] dc = new int[]{0, -1, 0, 1};

    #         boolean found = false;
    #         for (int i = 0; i < 4; ++i) {
    #             int nr = r + dr[i];
    #             int nc = c + dc[i];

    #             if (0 <= nr && nr < R && 0 <= nc && nc < C && !used[nr][nc]) {
    #                 List<Integer> next = min_path(M, nr, nc, used, k - 1);
    #                 if (!next.isEmpty()) {
    #                     result.add(M[r][c] + 1);
    #                     result.addAll(next);
    #                     found = true;
    #                     break;
    #                 }
    #             }
    #         }

    #         if (!found) {
    #             used[
