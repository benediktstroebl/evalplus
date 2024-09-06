from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'

    def traverse(current):
        if not current:
            return []
        result = []
        nesting_level = 1
        i = current.find(open_braces[nesting_level])
        while i >= 0:
            if paren_string[i:i+2] == open_braces[nesting_level]:
                result.append(current[:i])
                current = current[i+1:]
                traverse(current)
                break
            elif paren_string[i:i+2] == close_braces[nesting_level]:
                nesting_level += 1
                current = current[i+1:]
                i = current.find(open_braces[nesting_level])
            else:
                i = current.find(open_braces[nesting_level], i + 1)

        if current:
            result.append(current)
        return result
    
    return traverse(paren_string)