
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
    # check if the input planets are correct
    if planet1 not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    if planet2 not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
        return ()
    
    # check if the input planets are not the same
    if planet1 == planet2:
        return ()
    
    # get the list of planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # check if the orbits of the two planets are in the same direction
    if planet1 > planet2:
        # if the orbits are counterclockwise
        if planet1 > planet0 and planet1 < planet1b:
            # if the orbits are clockwise
            if planet0 > planet1 and planet0 > planet1b:
                # get the index of the closest planet
                index = np.argmin(np.abs(planet1 - planet0))
                planet0 = planets[index]
                planet1 = planets[planets.index(planet1)+1]
                # sort the planets by the proximity to the sun
                planets = [planets.index(p)+1 if p != planet0 else p for p in planets]
                # return the sorted planets
                return (planet0, planet1)
            else:
                # get the index of the closest planet
                index = np.argmin(np.abs(planet1 - planet0))
                planet0 = planets[index]
                planet1 = planets[planets.index(planet1)+1]
                # sort the planets by the proximity to the sun
                planets = [planets.index(p)+1 if p != planet0 else p for p in planets]
                # return the sorted planets
                return (planet0
