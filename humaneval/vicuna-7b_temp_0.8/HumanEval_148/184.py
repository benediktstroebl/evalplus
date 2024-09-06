
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

    # checking if the planets are correct
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    # finding the closest planet to the sun
    closest_planet = min(planet1.lower(), planet2.lower(), key=lambda x: distance(x, Earth))

    # finding the second closest planet to the sun
    second_closest_planet = max(planet1.lower(), planet2.lower(), key=lambda x: distance(x, Earth))

    # sorting all planets based on their distance from the sun
    planets = sorted(planet1.lower(), key=lambda x: distance(x, Earth), reverse=True)
    planets.insert(0, closest_planet)
    planets.insert(0, second_closest_planet)

    # returning the sorted list of planets
    return tuple(planets)
