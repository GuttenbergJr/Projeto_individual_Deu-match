candidatos = [
    ("candidato 1", "e5_t10_p8_s8"),
    ("candidato 2", "e10_t7_p7_s8"),
    ("candidato 3", "e8_t5_p4_s9"),
    ("candidato 4", "e2_t2_p2_s1"),
    ("candidato 5", "e10_t10_p8_s9")
]


def buscarCandidatos(notasMinimas):
    def verifica_notas(candidato):
        notasCandidato = [int(nota[1:]) for nota in candidato[1].split("_")]
        return all(notaCandidato >= notaMinima for notaCandidato, notaMinima in zip(notasCandidato, notasMinimas))

    candidatosSelecionados = filter(verifica_notas, candidatos)
    return [candidato[0] for candidato in candidatosSelecionados]

def main():

    notasMinimas = [
        int(input("Digite a nota mínima de entrevista: ")),
        int(input("Digite a nota mínima de teste teórico: ")),
        int(input("Digite a nota mínima de teste prático: ")),
        int(input("Digite a nota mínima de avaliação de soft skills: "))
    ]
    

    candidatosSelecionados = buscarCandidatos(notasMinimas)

    if candidatosSelecionados:
        print("Candidatos Selecionados: ")
        for candidato in candidatosSelecionados:
            print(candidato)
    else:
        print("Não há candidatos compatíveis com os critérios fornecidos.")

if __name__ == "__main__":
    main()
