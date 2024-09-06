
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Find the sum of all the even elements that are at odd indices
    # in the list and return that sum.
    #
    # If there are no odd indices, return 0.

    # 1. Brute-force solution:
    #    - O(n) time complexity
    #    - O(1) space complexity

    # sum = 0
    # for i in range(len(lst)):
    #     if i % 2 == 1 and lst[i] % 2 == 0:
    #         sum += lst[i]
    # return sum

    # 2. Space-optimized brute-force solution:
    #    - O(n) time complexity
    #    - O(1) space complexity

    # sum = 0
    # i = 1
    # while i < len(lst):
    #     if lst[i] % 2 == 0:
    #         sum += lst[i]
    #     i += 2
    # return sum

    # 3. One-liner:
    #    - O(n) time complexity
    #    - O(n) space complexity

    # return sum([lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0])

    # 4. Reasonably smart solution:
    #    - O(n) time complexity
    #    - O(1) space complexity

    # sum = 0
    # for i in range(1, len(lst), 2):
    #     if lst[i] % 2 == 0:
    #         sum += lst[i]
    # return sum

    # 5. Elegant solution:
    #    - O(n) time complexity
    #    - O(1) space complexity

    return sum(lst[i] for i in range(1, len(lst), 2) if lst[i] % 2 == 0)

