📚 Projeto de Análise de Livros e Avaliações
🎉 Bem-vindo ao seu projeto de análise de livros! 🚀

Este projeto foi desenvolvido para analisar um conjunto de dados de livros populares e avaliações de clientes utilizando o Streamlit. Com ele, é possível visualizar tendências de preços, ano de publicação, e explorar avaliações de livros em uma interface interativa e amigável.
🛠️ Funcionalidades

    Visão geral dos livros:
        Filtre livros por faixa de preço.
        Visualize gráficos de distribuição de preços e número de livros por ano de publicação.
    Página de Reviews:
        Selecione um livro específico para ver suas informações detalhadas, como preço, gênero, avaliação e ano de publicação.
        Leia as avaliações dos clientes em uma interface de chat interativa.

📁 Estrutura do Projeto

📂 ArquivosPython
├── topBooks.py             # Página principal para visualização de livros
├── pages/
│   └── 1_bookReview.py     # Página para visualizar as avaliações
├── customer reviews.csv    # Dataset com avaliações dos clientes
└── Top-100 Trending Books.csv # Dataset com informações dos livros

🚀 Como executar o projeto

Certifique-se de ter o Python instalado em sua máquina e siga os passos abaixo:
1. Clone o repositório:

git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO

2. Crie um ambiente virtual e ative-o:

# No Windows
python -m venv .venv
.venv\Scripts\activate

# No Linux ou macOS
python3 -m venv .venv
source .venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o projeto:

streamlit run topBooks.py

Após executar o comando, a aplicação será aberta automaticamente no seu navegador em http://localhost:8501.
🗃️ Dados Utilizados

    customer reviews.csv: Contém as avaliações de clientes para os livros.
        Colunas: book name, customer_name, review_title, review_content, rating.
    Top-100 Trending Books.csv: Contém informações sobre os livros populares.
        Colunas: book title, genre, book price, rating, year of publication.

📊 Demonstração

Aqui está uma prévia do que você verá ao rodar a aplicação:

    Página Principal (topBooks.py):

    Página de Reviews (1_bookReview.py):

📄 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo como desejar.
🤝 Contribuições

Contribuições são sempre bem-vindas! Se você deseja melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
