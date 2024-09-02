
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
    # planet1 = "Jupiter"
    # planet2 = "Neptune"
    # planet1 = "Earth"
    # planet2 = "Mercury"
    # planet1 = "Venus"
    # planet2 = "Uranus"
    # planet1 = "Mars"
    # planet2 = "Saturn"
    # planet1 = "Neptune"
    # planet2 = "Jupiter"
    # planet1 = "Uranus"
    # planet2 = "Earth"

    # planets = [[1, "Mercury"], [1, "Venus"], [1, "Earth"],
    # [1, "Mars"], [1, "Jupiter"], [1, "Saturn"], [1, "Uranus"]]

    planets = [[1, "Mercury"], [1, "Venus"], [1, "Earth"], [1, "Jupiter"],
            [1, "Mars"], [1, "Saturn"], [1, "Uranus"], [1, "Neptune"]]

    planet1_index = -1
    for i in range(len(planets)):
        if planets[i][1] == planet1:
            planet1_index = i
            break

    planet2_index = -1
    for i in range(len(planets)):
        if planets[i][1] == planet2:
            planet2_index = i
            break

    if planet1_index == -1 or planet2_index == -1:
        return ()

    orbit_planets = []
    for i in range(planet1_index, planet2_index):
        orbit_planets.append(planets[i][0])

    orbit_planets.sort()

    return tuple(orbit_planets)










