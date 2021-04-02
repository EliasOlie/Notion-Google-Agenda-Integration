import re
from typing import NamedTuple

class Resultado(NamedTuple):
    hora: str
    data: str
    local: str = None

def get_data(phrase: str) -> object:
    """
    Use regex to get info about some event trigged by "!" prefix
    """
    try:

        reghora = '[0-9]{2}:[0-9]{2}'

        dias = ['domingo','segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
        
        result_hora = re.search(reghora, phrase)
        pos_hora = result_hora.span()
        hora = phrase[pos_hora[0]:pos_hora[1]]

        for dia in dias:
            if dia in phrase:
                data = dia

        result_local = phrase.replace(hora, '')
        result_local = result_local.replace(data, '')
        
        result = Resultado(hora, data, result_local)
        
        return result
    except:
        return 'Algo deu errado e não era pra dar (eu acho)' #Tomara que não caia aqui!

