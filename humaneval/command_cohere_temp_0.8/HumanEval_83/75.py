```python
def starts_one_ends(n):
    # Create a list to store the results for 
	    # each number of digits from 1 to n
	    count = [0] * (n + 1)

	    # Calculate the count for each number of digits
	    for i in range(1, n + 1):
	        # Starting with 1 to n digits
		    count[i] += 10000000 // (10**i - 10**(i - 1))

	        # Removing trailing 1 from existing numbers
		    count[i] -= (10**i - 1) // (10**i - 9)

	        # Adding trailing 1 to existing numbers
		    count[i] += (10**i - 1) // (10**(i - 1) + 1)

	    return count[n]
```

The script provides a self-contained function `starts_one_ends(n)` designed to calculate the count of numbers that start or end with 1 within a given range. It employs mathematical operations to efficiently determine the count without the need for explicit number listing. The function is designed to work with positive integers only.