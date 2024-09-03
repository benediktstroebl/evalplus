def search(nums):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return max(freq)
nums = [4, 1, 2, 2, 3, 1]