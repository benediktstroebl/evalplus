
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
    # check if planet1 and planet2 are correct
    if planet1.lower() not in ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"] or planet2.lower() not in [
            "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]:
        return tuple()
    
    # check if the planets' orbits are located between the orbits of planet1 and planet2
    # use the gaps between the planets' orbits
    gaps = [(4.6 * (len(np.array(planet1.split(' ')) - np.array(planet2.split(' ')) + 1) + 1), 0) for planet1, planet2 in zip(planet1.split(' '), planet2.split(' '))]
    return tuple(sorted(gaps, key=lambda x: x[0]))
