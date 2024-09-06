def starts_one_ends(n):
    # Create a list to store the results for  1st position and last position
    count = [0, 0]
    
    # Check for the case when n = 1, in this case, only 1 exists
    if n == 1:
        return 1
    
    # Count the numbers that start with 1 or end with 1, without duplicates
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            num = str(i) + str(j) + '1'
            if num == '1' + str(n - 1):
                count[0] += 1
            elif num == '1' + str(i - 1) + '0':
                count[1] += 1
    
    return count[0] + count[1]