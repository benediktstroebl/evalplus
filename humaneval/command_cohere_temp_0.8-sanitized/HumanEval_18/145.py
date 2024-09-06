def how_many_times(string, substring):
    return len(string) - len(string.replace(substring, ''))