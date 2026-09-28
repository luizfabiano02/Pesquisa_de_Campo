# 📊 Pesquisa de Satisfação — 

Programa desenvolvido em **Python** para realizar uma pesquisa de satisfação com os clientes da empresa de marketing.

## 📌 Sobre o projeto

O programa realiza uma pesquisa com **50 entrevistados**, coletando:

* Nome;
* Idade;
* Opinião sobre o atendimento.

As opções de atendimento são:

```text
1 - EXCELENTE
2 - BOM
3 - RUIM
```

Ao final da pesquisa, o programa apresenta a quantidade de respostas:

* **EXCELENTE**
* **RUIM**

## 🔄 Funcionamento

O sistema realiza a pesquisa de forma repetitiva até completar os **50 entrevistados**.

Durante a pesquisa, cada resposta é analisada e as opções **EXCELENTE** e **RUIM** são contabilizadas.

Antes da execução completa, o programa pode ser testado com **10 entrevistados** para verificar seu funcionamento.

## 🧪 Teste

Para realizar o teste com 10 entrevistados, altere:

```python
for i in range(1, 51):
```

para:

```python
for i in range(1, 11):
```

Após concluir o teste, retorne para:

```python
for i in range(1, 51):
```

## ▶️ Execução

1. Abra o arquivo do programa no Python.
2. Execute o código.
3. Informe os dados solicitados para cada entrevistado.
4. Escolha uma das opções de atendimento.
5. Ao final, confira o resultado da pesquisa.

## 📋 Resultado

Ao finalizar os 50 entrevistados, será apresentado um resultado semelhante a:

```text
===================================
RESULTADO DA PESQUISA
===================================
Quantidade de respostas EXCELENTE: 25
Quantidade de respostas RUIM: 10
```

Os valores serão diferentes conforme as respostas registradas.

## 🛠️ Tecnologias

* Python 3

## 📚 Projeto acadêmico

**Curso:** Desenvolvimento de Sistemas
**Projeto:** Pesquisa de Satisfação — 
**Versão:** 1.0.0
