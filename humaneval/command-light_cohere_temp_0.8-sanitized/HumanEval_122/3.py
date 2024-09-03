def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
    Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    def test_add_elements():
        arr = [111, 121, 40000, 565, 678, 789, 8,9]
        k = 4
        result = add_elements(arr, k)
        expected = 24
        assert result == expected

        arr = [1000, 1001, 100, 101, 102, 103, 104, 105]
        k = 1
        result = add_elements(arr, k)
        expected = 500
        assert result == expected

        arr = [1000, 1001, 100, 101, 102, 103, 104, 105, 106]
        k = 2
        result = add_elements(arr, k)
        expected = 333
        assert result == expected

        arr = [1000, 1001, 100, 101, 102, 103, 104, 105, 200]
        k = 3
        result = add_elements(arr, k)
        expected = 222
        assert result == expected

        arr = [111, 121, 222, 333, 444, 555, 666]
        k = 4
        result = add_elements(arr, k)
        expected = 777
        assert result == expected

        arr = [1000, 1001, 100, 101, 102, 103, 104, 105, 200, 213]
        k = 5
        result = add_elements(arr, k)
        expected = 567
        assert result == expected

        return True

    test_add_elements()