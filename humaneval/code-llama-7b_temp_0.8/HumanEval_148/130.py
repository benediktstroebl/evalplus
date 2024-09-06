
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
    # planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # planets_lower = [planet.lower() for planet in planets]
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # planets_lower = [planet.lower() for planet in planets]
    planets_lower = ("mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune")
    planet1_index = 0
    planet2_index = 0
    if planet1 in planets_lower:
        planet1_index = planets_lower.index(planet1)
    if planet2 in planets_lower:
        planet2_index = planets_lower.index(planet2)
    if planet1_index == 0 or planet2_index == 7:
        return planets[1:3]
    if planet1_index == 1 or planet2_index == 6:
        return planets[2:4]
    if planet1_index == 2 or planet2_index == 5:
        return planets[3:6]
    if planet1_index == 3 or planet2_index == 4:
        return planets[4:6]
    if planet1_index == 4 or planet2_index == 3:
        return planets[5:7]
    if planet1_index == 5 or planet2_index == 2:
        return planets[6:8]
    if planet1_index == 6 or planet2_index == 1:
        return planets[7:8]
    if planet1_index == 7 or planet2_index == 0:
        return planets[0:3]
