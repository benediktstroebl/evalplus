from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    def balance(paren_string):
        """
        Determines if the paren_string is balanced or not.
        """
        depth = 0
        for paren in paren_string:
            if paren == '(':
                depth += 1
            elif paren == ')':
                if depth == 0:
                    return False
                depth -= 1
        return depth == 0

    def partition(paren_string):
        """
        Inputs a string of balanced parentheses and returns a list of string containing the balanced parentheses
        separated in groups.
        """
        if not paren_string:
            return []
        for idx, paren in enumerate(paren_string):
            if paren == '(':
                partitioned_string = paren_string[idx:]
                break
        else:
            return [paren_string]
        new_partitions = []
        for idx, paren in enumerate(partitioned_string):
            if paren == ')':
                new_partitions.append(partitioned_string[:idx + 1])
                partitioned_string = partitioned_string[idx + 1:]
                break
        if partitioned_string:
            new_partitions.extend(partition(partitioned_string))
        return new_partitions

    return partition(paren_string) if balance(paren_string) else [paren_string]

