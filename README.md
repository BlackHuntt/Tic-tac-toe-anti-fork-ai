# Tic-tac-toe-anti-fork-ai
iA Imbatível de jogo da Velha com heurística anti garfo customizada. Nunca Perde.

# 🧠 IA Gananciosa Anti-Garfo - Jogo da Velha

> Bot imbatível que NUNCA perde. Criado pra negar 100% das estratégias de garfo.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

## 🎯 Sobre o Projeto

Diferente do algoritmo Minimax tradicional que calcula todas as jogadas, essa IA usa **heurística gananciosa customizada** focada em negar armadilhas de "garfo" do adversário.

**Resultado:** Empata com Minimax em 100% das partidas e vence humanos desatentos.

## ⚔️ Como a Heurística Funciona?

A IA segue 4 regras de prioridade em cada jogada:

1. **VITÓRIA**: Se existe jogada pra ganhar, executa
2. **DEFESA**: Se o oponente pode ganhar no próximo lance, bloqueia  
3. **ANTI-GARFO**: Detecta se o inimigo pode criar um garfo e joga na posição que anula os 2 ataques simultaneamente
4. **CONTROLE**: Prioriza centro, depois cantos, depois laterais
5. Feito 100% no celular com logica pura mostrando que nao precisa de um pc lra codar so foco e vontade de aprender!

## 🚀 Como Executar

```bash
python ia_gananciosa.py
