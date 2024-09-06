def even_odd_count(num):
    if isinstance(num, int):
        # Remove non-digit characters from the input (assuming this is not an invalid input)
        num_str = str(num).strip('.!')
        count_odd = sum(1 for char in num_str if char % 2 != 0)
        count_even = sum(1 for char in num_str if char % 2 == 0)
        return count_odd, count_even
    else:
        raise ValueError("Input must be an integer")