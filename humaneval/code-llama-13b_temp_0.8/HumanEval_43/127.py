

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # 1. brute force solution
    # for each element in l, check if another element in l adds up to zero.
    # if so, return True. if not, return False.
    # O(n^2) runtime complexity.

    # 2. using set
    # for each element in l, check if the negative version of that element
    # is in l.
    # O(n) runtime complexity, but O(n) space complexity as well.

    # 3. using dictionary
    # for each element in l, check if the negative version of that element
    # is in l.
    # O(n) runtime complexity, O(n) space complexity.

    # 4. sort, then pointer solution
    # sort l. iterate thru l, starting at index i=0. set pointer j=len(l) - 1.
    # check if l[i] + l[j] == 0. if so, return True. if not, and if i < len(l) - 1,
    # increment i. otherwise, decrement j.
    # O(nlogn) runtime complexity, O(1) space complexity.

    # 5. sort, then binary search solution
    # sort l. iterate thru l, starting at index i=0. set pointer j=len(l) - 1.
    # check if l[i] + l[j] == 0. if so, return True. if not, and if i < len(l) - 1,
    # increment i. otherwise, decrement j.
    # O(nlogn) runtime complexity, O(1) space complexity.

    # 6. hashmap solution
    # iterate thru l, adding each element in l to a dictionary, where the key is
    # the element and the value is the index of that element.
    # iterate thru l, starting at index i=1. check if -l[i] is in the dictionary.
    # if so, return True. if not, return False.
    # O(n) runtime complexity, O(n) space complexity.

    # 7. two-pointer solution
    # sort l. use pointer i=0 and
