The provided Python script defines a function **`filter_by_substring`** that efficiently filters an input list of strings for those containing a specific substring. The function utilizes Python's **`List`** and **`str`** modules and implements a test-driven approach to solve the problem:

Here's a breakdown of the function:
- The function **`filter_by_substring`** takes two parameters:
	- **`strings:`** - A list of strings to filter.
	- **`substring:`** - The substring to search for within the strings in **`strings`** 

The function utilizes a **`List`** comprehension to iterate through each string in the input list:
- For each string, it checks if the beginning of the string matches the **`substring`**. If a match is found, the string is added to the resulting filtered list. 

In essence, the function provides an effective way to filter and retrieve strings from a given list that contain a specific substring.