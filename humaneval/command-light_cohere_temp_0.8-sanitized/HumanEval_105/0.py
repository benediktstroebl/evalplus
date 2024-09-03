def by_length(arr):
    if not arr:  # checks for empty array
        return []
    
    # filter out numbers outside the range of one to nine
    filtered = [x for x in arr if 1 <= x <= 9]
    
    # sort the filtered array
    sorted_filtered = sorted(filtered)
    
    # reverse the sorted array
    reversed_filtered = sorted_filtered[::-1]
    
    # map each digit to its corresponding name
    mapped_digits = { digit: 'One' for digit in reversed_filtered }
    
    return mapped_digits()