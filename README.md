# 🛒 Automação de Cadastro de Produtos

Este projeto é uma automação desenvolvida em **Python** para agilizar e padronizar o processo de cadastro de produtos em sistemas internos.  
A ferramenta lê os dados de uma planilha, faz validações e utiliza **PyAutoGUI** para realizar o cadastro automaticamente na interface, reduzindo o tempo gasto e minimizando erros manuais.

---

## ✨ Funcionalidades

- 📥 **Importação de dados** (Excel/CSV)  
- 🔍 **Validação e padronização** das informações antes do cadastro  
- 🖱️ **Automação da interface** usando PyAutoGUI para preencher os campos do sistema  
- 🧩 **Tratamento de falhas** e mensagens de log  
- ⚙️ **Configuração simples** e fácil de adaptar para outros sistemas ou fluxos

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **PyAutoGUI**
- **Pandas**
- **OpenPyXL**
- *(Inclua outras libs se necessário)*

---

## 🚀 Como executar

### Instale as dependências

As bibliotecas necessárias para rodar a automação são:

- **PyAutoGUI**
- **Pandas**
- **OpenPyXL**

Você pode instalar todas de uma vez com:

```bash
pip install pyautogui pandas openpyxl
```

### 🗂️ Prepare sua planilha de produtos

- Verifique se as colunas estão corretas  
- Ajuste o caminho do arquivo no código, se necessário  

---

### ▶️ Execute a automação

```bash
python automacao.py
```

## 📁 Estrutura do projeto

    📂 Automacao-Cadastro-de-Produtos
        ├── automacao.py
        ├── produtos.csv
        ├── position.py
        └── README.md

## 🎯 Objetivo do projeto

Este projeto foi criado para facilitar tarefas repetitivas e demonstrar conhecimentos em:

- Automação de processos  
- Manipulação de dados  
- Boas práticas em Python  
- Otimização de rotinas operacionais  

## 📝 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.
