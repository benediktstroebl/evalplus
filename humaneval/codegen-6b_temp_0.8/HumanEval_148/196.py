
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
    # refactored from Christopher Barnard's solver
    if planet1 == "Sun":
        return planet2
    elif planet2 == "Sun":
        return planet1
    elif planet1 not in names or planet2 not in names:
        return ()

    planets = set()
    name_to_orbit = {name: planet_orbit(name) for name in names}
    for planet_orbit in name_to_orbit.values():
        while planet_orbit.parent:
            planets.add(planet_orbit.parent)
            planet_orbit = planet_orbit.parent
        while planet_orbit not in planets:
            planets.add(planet_orbit)
            planet_orbit = planet_orbit.parent
    planets = set(name_to_orbit[planet] for planet in planets)
    for planet in planets:
        if planet.parent is None:
            print(planet)
            print(" these are all planets that orbit the sun")

    def cost(planet):
        if planet.name == planet2:
            return planet.orbit_length
        else:
            return 1 + min(cost(c) for c in planet.children)
    path = list(sorted(planets, key=cost))
    if planet1 == planet2:
        return tuple(path)
    next = planet2
    path.remove(planet1)
    for planet in path:
        if planet.name == next:
            return tuple(path) + (planet,)
        next = planet

    return ()
