
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    """
    var nums = array.length;
    var tmp = [], carry = 0;
    nums += 1;
    for (var i = 1; i <= nums; ++i) {
        var carry = 0;
        var sum = array[i] + carry;
        if (sum < 0 || sum > 9) {
            carry = sum / 10;
            sum = sum % 10;
        }
        else {
            carry = 0;
        }
        tmp[i] = sum;
        if (i == nums) {
            tmp[0] += carry;
        }
    }
    return tmp;
    """
    nums = len(array)
    cum_sum = [0] * (nums + 1)
    for i, v in enumerate(array):
        cum_sum[i+1] = array[i] + cum_sum[i]
    ans = []
    carry = 0
    for i in range(nums, 0, -1):
        if cum_sum[i] == carry:
            ans.append(0)
        else:
            ans.append(cum_sum[i] - carry)
        carry = cum_sum[i]
    if carry:
        ans.append(carry)
    return list(reversed(ans))
    
assert sort_array([]) == []
assert sort_array([5]) == [5]
assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
assert sort_array([1, 2, 2, 3, 3]) == [1, 2, 2, 3, 3]

assert sort_array([3, 2, 3, 4]) == [3, 2, 3, 4]
assert sort_array([3, 6, 2]) == [2, 3, 6]
assert sort_array([3, 6]) == [3, 6]
assert sort_array([2]) == [2]
assert sort_array([1, 2