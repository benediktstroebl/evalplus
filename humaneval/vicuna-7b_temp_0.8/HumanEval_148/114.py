
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
    if not planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []
    if not planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return []

    planet_list = [planet1, planet2]
    planet_list.sort(key=lambda x: (x.distance_to(sun), x))

    sun_distance = 0
    planets = []
    for i in range(len(planet_list) - 1):
        planet_i = planet_list[i]
        planet_j = planet_list[i + 1]
        if planet_i.distance_to(sun) <= 1.5 * planet_j.distance_to(sun):
            planets.append(planet_i)
            sun_distance = planet_i.distance_to(sun)
        elif planet_j.distance_to(sun) < 2.0 * planet_i.distance_to(sun):
            planets.append(planet_j)
            sun_distance = planet_j.distance_to(sun)

    return planets

planet1 = input("Enter first planet name: ")
planet2 = input("Enter second planet name: ")
planets = bf(planet1, planet2)
