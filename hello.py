import pandas as pd
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
df = get_df("books_csv")  # Load data
df["average_rating"] = pd.to_numeric(df["average_rating"], errors="coerce")
df["text_reviews_count"] = pd.to_numeric(df["text_reviews_count"], errors="coerce")

sql = "SELECT title, authors, average_rating, ratings_count, text_reviews_count FROM books_csv WHERE CAST(average_rating as REAL) > 4.35"
filtered_df = query(sql, "books_csv")

text("# A quick exploration into a Goodreads Books dataset")
text("## Goodreads Books with Rating > 4.35")
text("Selected this value to try to keep the number of results small enough to view in one page.")
table(filtered_df, title="Filtered Data")


text("## Average Rating vs. Number of Text Reviews")
text("Exploring the idea that there are more written reviews for higher rated books.")
fig = px.scatter(df, x="text_reviews_count", y="average_rating", log_x=True)
fig.update_xaxes(
    type="log",
    tickvals=[10,100, 1000, 10000, 100000],
    ticktext=["10", "100", "1000", "10000", "100000"]
)
plotly(fig)


