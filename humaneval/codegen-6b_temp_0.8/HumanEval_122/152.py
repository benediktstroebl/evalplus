
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    def helper(arr, k, result):
        if k == 0:
            return result
        single_digits = {}
        for i in range(len(arr)):
            s = str(arr[i])
            if int(s[0]) in single_digits:
                single_digits[int(s[0])] += 1
            else:
                single_digits[int(s[0])] = 1
            if len(s) > 1:
                if s[1] in single_digits:
                    single_digits[s[1]] += 1
                else:
                    single_digits[s[1]] = 1

        for key in single_digits:
            if single_digits[key] <= k:
                result += key * single_digits[key]
                k -= single_digits[key]

        two_digits = {}
        for i in range(len(arr)):
            key = arr[i] // 10
            value = arr[i] % 10

            if key in two_digits:
                two_digits[key] += value
            else:
                two_digits[key] = value

            if key * 10 + 1 in two_digits:
                two_digits[key * 10 + 1] += value
            else:
                two_digits[key * 10 + 1] = value

            if key * 10 + 2 in two_digits:
                two_digits[key * 10 + 2] += value
            else:
                two_digits[key * 10 + 2] = value

            if key * 10 + 3 in two_digits:
                two_digits[key * 10 + 3] += value
            else:
                two_digits[key * 10 + 3] = value

            if key * 10 + 4 in two_digits:
                two_digits[key * 10 + 4] += value
            else:
                two_digits[key * 10 + 4] = value

            if key * 10 + 5 in two_digits:
                two_digits[key * 10 + 5] += value
            else:
                two_digits[key *