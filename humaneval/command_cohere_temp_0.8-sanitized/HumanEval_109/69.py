def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    # Test cases part
    def test_empty_arr(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([5]))

    def test_multiple_elements_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_multiple_elements_not_sorted(self):
        self.assertFalse(move_one_ball([4, 2, 1, 3, 5]))

    def test_multiple_elements_with_duplicates(self):
        self.assertFalse(move_one_ball([2, 4, 3, 2, 1, 5]))

    def test_large_array(self):
        large_arr = list(range(1, 1001))
        large_arr.sort()
        self.assertTrue(move_one_ball(large_arr))

    def test_large_array_unlucky_shuffle(self):
        large_arr = list(range(1, 1001))
        large_arr.sort(reverse=True)
        self.assertFalse(move_one_ball(large_arr))

    return {
        'tests': [test_empty_arr, test_single_element, test_multiple_elements_sorted,
                   test_multiple_elements_not_sorted, test_multiple_elements_with_duplicates,
                   test_large_array, test_large_array_unlucky_shuffle
                   ],
        'move_one_ball': move_one_ball
    }