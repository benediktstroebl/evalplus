
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
    
    planet1 = planet1.lower()
    planet2 = planet2.lower()

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Convert planet names to lowercase
    for i in range(len(planets)):
        planets[i] = planets[i].lower()

    # Calculate the positions of the planets
    positions = []
    for i in range(len(planets)):
        if planets[i] == planet1:
            positions.append(i)
        if planets[i] == planet2:
            positions.append(i)
        
    # Calculate the lists of positions
    pos1 = []
    for p in positions:
        pos1.append(p - positions[0])
    pos2 = []
    for p in positions:
        pos2.append(p - positions[-1])

    # Sort the list by position
    i = 0
    while i < len(pos1):
        j = i + 1
        while j < len(pos1):
            if pos1[i] > pos1[j]:
                temp = pos1[i]
                pos1[i] = pos1[j]
                pos1[j] = temp
                temp = pos2[i]
                pos2[i] = pos2[j]
                pos2[j] = temp
            j = j + 1
        i = i + 1

    # Remove duplicate positions
    i = 1
    while i < len(pos1):
        if pos1[i] == pos1[i-1]:
            pos2.remove(pos2[i])
        else:
            i = i + 1

    # Return a tuple of sorted planet names
    return tuple(planets[i] for i in pos2)
