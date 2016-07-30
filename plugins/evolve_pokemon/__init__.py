from pokemongo_bot.human_behaviour import sleep
from pokemongo_bot.event_manager import manager
from pokemongo_bot import logger


@manager.on("evolve_pokemon", priority=1000)
def transfer_pokemon(bot, evolve_list=None):
    # type: (PokemonGoBot, Optional[List[Pokemon]]) -> None

    def log(text, color="black"):
        logger.log(text, color=color, prefix="Evolve")

    if evolve_list is None or len(evolve_list) == 0:
        log("No Pokemon to evolve.", color="yellow")

    for index, pokemon in enumerate(evolve_list):
        pokemon_num = pokemon.pokemon_id
        pokemon_name = bot.pokemon_list[pokemon_num - 1]["Name"]
        pokemon_cp = pokemon.combat_power
        pokemon_potential = pokemon.potential
        log("Evolving {0} (#{1}) with CP {2} and IV {3} ({4}/{5})".format(pokemon_name,
                                                                          pokemon_num,
                                                                          pokemon_cp,
                                                                          pokemon_potential,
                                                                          index+1,
                                                                          len(evolve_list)))

        bot.api_wrapper.evolve_pokemon(pokemon_id=pokemon.unique_id).call()
        sleep(2)

    log("Evolved {} Pokemon.".format(len(evolve_list)))
