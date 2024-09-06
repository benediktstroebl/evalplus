
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

    # Check if the input planets are valid
    if not "Mercury" <= planet1 <= "Neptune":
        return []
    if not "Mercury" <= planet2 <= "Neptune":
        return []

    # Find the index of the planet
    planet_index = "Mercury" <= planet1
    if planet1 < "Mercury":
        planet1 = "Mercury"
        planet_index = 0
    elif planet1 > "Neptune":
        planet1 = "Neptune"
        planet_index = 7

    planet2_index = "Mercury" <= planet2
    if planet2 < "Mercury":
        planet2 = "Mercury"
        planet2_index = 0
    elif planet2 > "Neptune":
        planet2 = "Neptune"
        planet2_index = 7

    # Find the orbits of the planets
    planet_semi_major_axis1 = ABS(planet1 - "Sun")
    planet_semi_major_axis2 = ABS(planet2 - "Sun")

    # Find the closest planet
    min_distance = float('inf')
    min_index = 0
    for i in range(0, 8):
        if i == planet1_index:
            continue
        if planet1[i] == "N" or planet1[i] == "N" or planet2[i] == "Y" or planet2[i] == "Y":
            continue
        if abs(planet1[i] - planet2[i]) < min_distance:
            min_distance = abs(planet1[i] - planet2[i])
            min_index = i

    # Find the index of the closest planet
    index = min_index

    # Find the orbits of the planets
    planet_semi_major_axis1 = ABS(planet1[index] - "Sun")
    planet_semi_major_axis2 = ABS(planet2[index] - "Sun")

    # Find the closest planet
    min_distance =
