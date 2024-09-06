def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with the supplied string."""
    max_len = len(string) // 2 + 1 if len(string) % 2 == 0 else len(string) // 2
    palindic_suffix = ''.join(sorted(string[-max_len:])) if max_len < len(string) else ''

    return f"{string}{palindic_suffix}{string[::-1][:len(string) - max_len - 1]}{palindic_suffix[::-1] if palindic_suffix else ''}"