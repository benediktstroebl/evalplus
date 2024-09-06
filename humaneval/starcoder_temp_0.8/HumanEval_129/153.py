
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
    # 这道题目是Hard的，但是思路是很清晰的
    # 如何实现一个K长度的路径，就是找最短的一条路径，
    # 这个路径是经过了K个点，每个点都在二维数组的边界，如果是上下左右，那么就是K的。
    # 所以我们的思路就是找到这条最短的路径，然后对他进行从大到小的排序，这样就得到了K长度的路径
    # 寻找最短路径的思路是经典的BFS，从一个节点开始，如果该节点是可达的，那么就把他加入队列中，然后从队列中取出一个节点，然后对他的所有边进行遍历，如果可达，则把他加入队列中，如果不可达，则跳过，不加入队列中，直到队列为空，算法结束。
    # 时间复杂度是O(K * N^2 * M)
    # 空间复杂度是O(N^2 * M)
    # K是路径的长度，N是行数，M是列数
    def bfs(start_node, k):
        visited = set()
        queue = [start_node]
        level = 1
        # 存储路径的节点
        path_node_list = []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if level == k:
                    path_node_list.append(node)
                visited.add(node)
                # 遍历边
                for child_node in children(node, grid):
                    if child_node not in visited:
                        queue.append(child_node)
            level += 1
        # 对每个节点的坐标进行排序
        path_list = []
        for node in path_node_list:
            path_list.append(node[0] * m + node[1])
        path_list.sort()
        # 把path_list中的值转化为坐标值
        result = []
        for val in path_list:
            x = val // m
            y = val % m
            result.append(grid[x][y])
        return result
    def children(node, grid):
        row, col = node
        children = []
        if row - 1 >= 0
