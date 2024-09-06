
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
    correct_planets = []
    incorrect_planets = []

    if not planet1.startswith("Mer") and not planet1.startswith("Ven"):
        incorrect_planets.append(planet1)

    if not planet2.startswith("Jup") and not planet2.startswith("Sat"):
        incorrect_planets.append(planet2)

    if not incorrect_planets:
        return incorrect_planets

    other_planets = []
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        if planet not in incorrect_planets:
            other_planets.append(planet)

    if not other_planets:
        return incorrect_planets

    sorted_planets = sorted(incorrect_planets + other_planets, key=lambda planet: 1 / (planet.l**2 + planet.a**2 - Sun.l**2))

    return tuple(sorted_planets)
