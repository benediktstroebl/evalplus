
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
    if not is_valid_planet_name(planet1) or not is_valid_planet_name(planet2):
        return ()

    planets = []

    # Find the closest planet to the sun and record its name
    closest_planet = min(planet1, planet2)
    if is_valid_planet_name(closest_planet):
        planets.append(closest_planet)

    # Find all planets with orbits between the orbit of the closest planet
    # and the orbit of the second closest planet
    for planet in planet1:
        if is_valid_planet_name(planet) and planet not in planets:
            planets.append(planet)

    # Find all planets with orbits between the orbit of the second closest planet
    # and the orbit of the closest planet
    for planet in planet2:
        if is_valid_planet_name(planet) and planet not in planets:
            planets.extend(planet for planet in planet1 if planet in planet)

    # Sort the planets by their proximity to the sun
    sorted_planets = sorted(planets, key=lambda x: x.distance_to(sun))

    return tuple(sorted_planets)
