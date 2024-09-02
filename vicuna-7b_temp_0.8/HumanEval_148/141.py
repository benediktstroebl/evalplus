
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
    if not(planet1 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return []
    if not(planet2 in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
        return []
    
    # check if the orbit of the first planet is less than the orbit of the second planet
    if planet1 < planet2:
        planets = [planet1]
        for i in range(1, len(planets)):
            # check if the orbit of the current planet is greater than the orbit of the second planet
            if planets[i] > planet2:
                break
            # check if the orbit of the current planet is less than the orbit of the second planet
            elif planets[i] <= planet2:
                planets.append(planets[i])
        return sorted(planets, key=lambda x: abs(x - sun))
    else:
        # the orbit of the first planet is greater than the orbit of the second planet
        # check if the orbit of the second planet is less than the orbit of the first planet
        if planet2 < planet1:
            planets = [planet2]
            for i in range(1, len(planets)):
                # check if the orbit of the current planet is greater than the orbit of the first planet
                if planets[i] > planet1:
                    break
                # check if the orbit of the current planet is less than the orbit of the first planet
                elif planets[i] <= planet1:
                    planets.append(planets[i])
            return sorted(planets, key=lambda x: abs(x - sun))
        else:
            # the orbit of the first planet is greater than the orbit of the second planet and the orbit of the second planet is greater than the orbit of the first planet
            # return an empty tuple
            return []
