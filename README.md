# Transformação de Sequência de Prüfer em Árvore e Processo Inverso

Este repositório contém algoritmos que realizam a transformação de uma **sequência de Prüfer** em sua árvore correspondente, além de realizar o processo inverso, ou seja, a conversão de uma árvore em sua sequência de Prüfer.

## Introdução

O **código de Prüfer** é uma maneira eficiente de representar árvores. Ele está diretamente relacionado à fórmula de **Cayley**, que afirma que existem \(n^{(n-2)}\) árvores geradoras para \(n\) vértices.

Para cada sequência de Prüfer, existe uma **única árvore** relacionada a ela. Portanto, como existem \(n^{(n-2)}\) sequências de Prüfer para \(n\) vértices, também existem \(n^{(n-2)}\) árvores geradoras possíveis para \(n\) vértices.

## Objetivo

Este repositório implementa os seguintes algoritmos:
- Transformação de uma **sequência de Prüfer** em uma **árvore geradora**.
- Processo **inverso**: conversão de uma árvore geradora em sua **sequência de Prüfer**.

## Contexto Acadêmico

Este trabalho foi realizado como parte da disciplina de **Teoria dos Grafos**, no curso de **Engenharia da Computação** da **Universidade Federal de Alagoas** (UFAL).

## Fórmula de Cayley

A fórmula de Cayley estabelece que o número de árvores geradoras para um grafo completo com \(n\) vértices é dado por:

\[ n^{(n-2)} \]

## Referências

- “Graduate Texts in Mathematics”, J. A. Bondy & U. S. R. Murty. Lançado em 2008.

---

# Prüfer Sequence to Tree Transformation and Inverse Process

This repository contains algorithms that transform a **Prüfer sequence** into its corresponding tree, as well as the reverse process, which converts a tree back into its Prüfer sequence.

## Introduction

The **Prüfer code** is an efficient way to represent trees. It is directly related to **Cayley's formula**, which states that there are \(n^{(n-2)}\) spanning trees for \(n\) vertices.

For each Prüfer sequence, there is a **unique tree** associated with it. Therefore, since there are \(n^{(n-2)}\) Prüfer sequences for \(n\) vertices, there are also \(n^{(n-2)}\) spanning trees possible for \(n\) vertices.

## Objective

This repository implements the following algorithms:
- Transformation of a **Prüfer sequence** into a **spanning tree**.
- **Reverse process**: converting a spanning tree into its **Prüfer sequence**.

## Academic Context

This work was developed as part of the **Graph Theory** course, in the **Computer Engineering** program at the **Federal University of Alagoas** (UFAL).

## Usage Instructions

1. Clone the repository.
2. Compile the files and run the algorithms as described in the instruction file.

## Cayley's Formula

Cayley's formula states that the number of spanning trees for a complete graph with \(n\) vertices is given by:

\[ n^{(n-2)} \]

## References
“Graduate Texts in Mathematics”, J. A. Bondy & U. S. R. Murty; 2008.
