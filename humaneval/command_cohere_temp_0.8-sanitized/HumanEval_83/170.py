def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number with n-1 values between 1 and 9.
    dp = [0] * (n - 1)

    # Count the numbers that start with 1
    dp[0] = 1

    # Use a recursive approach to count the numbers that end with 1
    for i in range(1, n - 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + 1) * 10

    # Remove duplicates by subtracting the counts of numbers that start with 1
    for i in range(n - 2, -1, -1):
        dp[i] -= dp[i] // 10  # Adjust the count by subtracting the overlapping counts

    return dp[0]