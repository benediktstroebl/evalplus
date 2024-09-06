

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    # Define empty dict to store the prime values
    prime_dict = {}
    # Define empty list to store the sum of digits
    digit_sum_list = []
    # Define empty list to store the current sum
    current_sum = []
    # Define variable to store the largest prime value
    largest_prime = -1
    # Loop through the list
    for num in lst:
        # Check if the number is prime
        if num > 1:
            if num not in prime_dict:
                prime_dict[num] = 1
                # If the number is prime, it means we are at the start of a new prime
                if largest_prime < num:
                    largest_prime = num
            else:
                # If the number is not prime, then we are not at the start of a new prime
                current_sum = sum(prime_dict[p] for p in prime_dict if p <= num)
                # Calculate the sum of digits of the current sum
                digit_sum = sum(int(d) for d in str(current_sum))
                # Add the current sum to the digit_sum_list
                digit_sum_list.append(current_sum)
                # If the current sum is the largest prime value, update the largest prime value and the current sum
                if current_sum == largest_prime:
                    largest_prime = num
                    current_sum = sum(prime_dict[p] for p in prime_dict if p <= num)
                # If the current sum is not the largest prime value, update the current sum
                elif current_sum < largest_prime:
                    current_sum += num
    # If the largest prime value is not stored in the prime_dict, it means it is not prime
    if largest_prime not in prime_dict:
        # Add the largest prime value to the prime_dict
        prime_dict[largest_prime] = 1
        # Calculate the sum of digits of the largest prime value
        digit_sum = sum(int(d) for d in str(largest_prime))
        # Add the largest prime value to the digit_sum_list
        digit_sum_list.append(largest_prime)
    # Calcul
