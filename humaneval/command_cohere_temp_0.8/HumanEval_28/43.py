```python
# Retrieve the input list of strings
function concatenate(strings: List<string>) : string {
    // Concatenate the strings in the list
    let result : string = ""
    for string in strings {
        result += string
    }
    return result
}
```