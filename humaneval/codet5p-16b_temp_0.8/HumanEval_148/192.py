
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

    planet1_orbit = {
        "Mercury":    58,
        "Venus":        108,
        "Earth":        149.6,
        "Mars":        227.9,
        "Jupiter":    778.7,
        "Saturn":    1429.5,
        "Uranus":    2872.5,
        "Neptune":    4497.7
    }
    planet2_orbit = {
        "Mercury":    58,
        "Venus":        108,
        "Earth":        149.6,
        "Mars":        227.9,
        "Jupiter":    778.7,
        "Saturn":    1429.5,
        "Uranus":    2872.5,
        "Neptune":    4497.7
    }

    for planet, orbit in planet1_orbit.items():
        if planet1 == planet:
            planet1_orbit[planet] = orbit
    for planet, orbit in planet2_orbit.items():
        if planet2 == planet:
            planet2_orbit[planet
