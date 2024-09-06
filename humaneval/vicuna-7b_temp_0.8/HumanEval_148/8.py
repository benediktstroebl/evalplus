
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
    # check if the planets are valid
    if planet1 == "Mercury" or planet1 == "Venus" or planet1 == "Earth" or planet1 == "Mars" or planet1 == "Jupiter" or planet1 == "Saturn" or planet1 == "Uranus" or planet1 == "Neptune":
        return (planet1,)
    if planet2 == "Mercury" or planet2 == "Venus" or planet2 == "Earth" or planet2 == "Mars" or planet2 == "Jupiter" or planet2 == "Saturn" or planet2 == "Uranus" or planet2 == "Neptune":
        return ()

    # find the distance between the planets in astronomical units (AU)
    a = distance(planet1, planet2)

    # find the closest planet
    closest = None
    closest_distance = a
    for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        d = distance(planet, planet2)
        if d < closest_distance:
            closest = planet
            closest_distance = d

    # find all the planets between the two given planets
    planets = []
    if closest:
        for planet in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
            if distance(planet, closest) < a:
                planets.append(planet)

    # sort the planets by proximity to the sun
    planets.sort(key=lambda x: (solar_distance(x), x))

    return planets
