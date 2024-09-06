
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    d = {
        "Mercury":(-2 * math.pi - 2 * math.pi / 365 - math.pi / (365 * 1.496e11), 0),
        "Venus":(-math.pi - 2 * math.pi / 365 - math.pi / (365 * 1.496e11), -math.pi / (365 * 1.496e11), math.pi / (365 * 1.496e11), 0),
        "Earth":(-math.pi - 2 * math.pi / 365, -math.pi / (365 * 1.496e11), math.pi / (365 * 1.496e11), 0),
        "Mars":(-2 * math.pi - 2 * math.pi / 365 - math.pi / (365 * 6.371e6), -2 * math.pi / (365 * 6.371e6), -3 * math.pi / (365 * 6.371e6), -math.pi / (365 * 6.371e6), -math.pi / (365 * 6.371e6)),
        "Jupiter":(-3 * math.pi - 2 * math.pi / 365 - math.pi / (365 * 1.496e11), -math.pi / (365 * 1.496e11), -math.pi / (365 * 1.496e11), -2 * math.pi / (365 * 1.496e11), -3 * math.pi / (365 * 1.496e11), -4 * math.pi / (365 * 1.496e11)),
        "Saturn":(-4 * math.pi - 2 * math.pi / 365 - math.pi / (365 * 1.496e11), -3 * math.pi / (365 * 1.496e11), -3 * math.pi / (365 * 1.496e11), -2 * math.pi / (365 * 1.496e11), -4 * math.pi / (365 * 1.496e11), -5 * math.pi / (365 * 1.496e11), -6 * math.pi / (365 * 1.496e11)),
        "Uranus":(-5 * math.pi - 2 * math.pi / 365 - math.pi / (365 * 1.