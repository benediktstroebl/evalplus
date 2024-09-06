```python
# Retrieve the input list of strings
function concatenate(strings: List<string>) : string {
    // Verify the input list is not empty
    if (strings.length == 0) {
        // If the list is empty, return an empty string
        return ''
    }

    // Initialize the result variable to concatenate all strings in the list
    let result: string = strings[0]
    for i in range(1, strings.length) {
        // Concatenate the current string with the result variable
          result = result.concat(strings[i])
    }
    return result
}
```