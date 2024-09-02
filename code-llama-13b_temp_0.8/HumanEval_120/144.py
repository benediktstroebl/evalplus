
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # 考虑最简单的情况，将 k 个数存到堆中，如果第 k + 1 个数大于堆顶，则弹出堆顶并且将第 k + 1 个数放进堆中。
    # 这里的最大堆我们用数组实现，其中每个数的位置就是其在堆中的位置，因此数组的第 i 个位置代表了一个堆中的数，
    # 其父亲在位置 (i - 1) // 2，子亲分别在位置 2 * i + 1 和 2 * i + 2 ，堆顶在位置 0 。
    # 最终的时间复杂度为 O(k * log(k))，k 个元素进堆的时间为 O(k * log(k))，此外调用 heapq.heapreplace 的时间为 O(log(k))
    # 实际上，如果我们可以修改堆的实现方式，使得 heapreplace 的时间为常数，那么整个算法的时间复杂度为 O(k)。
    # 而 heapq 模块只提供了两个操作 - 将一个元素放入堆中的 heapq.heappush 和 将堆顶元素弹出并且替换为新的元素的 heapq.heapreplace。
    # 因此，我们需要实现一个可以 heapreplace 的堆。堆的实现可以采用数组来实现，当我们要将一个元素从一个位置移动到另一个位置时，
    # 我们只需要改变被移动元素以及被移动元素
