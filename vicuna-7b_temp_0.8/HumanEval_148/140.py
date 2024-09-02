
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
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"] or planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet1 < "Mercury":
        return ()
    if planet1 > "Saturn":
        return ()
    if planet2 < "Mercury":
        return ()
    if planet2 > "Saturn":
        return ()
    # calculate the distance from the sun to each planet
    planets = [Distance.of_planet(p) for p in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]]
    # sort the planets by their distance from the sun
    planets.sort()
    # return all the planets whose orbits are between the orbit of planet1 and the orbit of planet2
    return tuple(planets[i for i in range(len(planets)) if Distance.of_planet(planet1) < Distance.of_planet(planets[i]) <= Distance.of_planet(planet2)] if Distance.of_planet(planet1) < Distance.of_planet(planet2))