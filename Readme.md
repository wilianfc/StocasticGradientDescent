# Stocastic Gradient Descent - Exemplo

A função de taxa de aprendizagem ηt = ηimin + 1/2(ηimax − ηimin)(1 + cos(Tcur/Tiπ)) é uma função cíclica que ajusta a taxa de aprendizagem do modelo durante o processo de treinamento. 

Onde:
- ηt é a taxa de aprendizagem no tempo t
- ηimin é a taxa de aprendizagem mínima
- ηimax é a taxa de aprendizagem máxima
- Tcur é o número da época atual de treinamento
- Ti é o número total de épocas em um ciclo completo

A função começa com uma taxa de aprendizagem mínima e aumenta gradualmente até a taxa máxima no meio do ciclo. Em seguida, diminui gradualmente até a taxa mínima no final do ciclo. Isso ajuda a evitar que o modelo fique preso em mínimos locais e permite que ele explore mais o espaço de parâmetros.

O parâmetro Ti é o número total de épocas em um ciclo completo, e é geralmente definido como uma fração do número total de épocas de treinamento. Por exemplo, se o modelo for treinado por 100 épocas e Ti for definido como 10, um ciclo completo será executado a cada 10 épocas.

A função cos(Tcur/Tiπ) é usada para controlar a taxa de mudança da taxa de aprendizagem durante o ciclo. Quando Tcur está próximo de 0 ou Ti, a taxa de mudança é baixa, o que permite que o modelo explore mais o espaço de parâmetros. Quando Tcur está no meio do ciclo, a taxa de mudança é alta, o que permite que o modelo ajuste seus parâmetros com mais precisão.