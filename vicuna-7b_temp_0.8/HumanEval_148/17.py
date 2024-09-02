
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

    if not is_planet(planet1) or not is_planet(planet2):
        return ()
    if planet1 < planet2:
        planet2, planet1 = planet1, planet2

    planets = []
    next_nearest_planet = planet1
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        if is_planet(planet) and planet.semi_major_axis < next_nearest_planet.semi_major_axis:
            planets.append(planet)
            next_nearest_planet = planet
        elif is_planet(planet) and planet.semi_major_axis >= next_nearest_planet.semi_major_axis:
            planets.append(planet)
            next_nearest_planet = planet

    planets.sort(key=lambda x: x.semi_major_axis - sun_distance)

    return tuple(planets)
