

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(x <= t for x in l)

def print_config(cfg: Config):
    """Print the configuration file."""
    for section in cfg.sections():
        print(f"{section}:")
        for option in cfg.options(section):
            value = cfg.get(section, option)
            print(f"  {option} => {value}")