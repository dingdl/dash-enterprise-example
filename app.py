# import dash
from dash import html, Dash


app = Dash(__name__)
server = app.server
app.layout = html.Div(
    children=html.H1(
        children=['This is a Dash app!']
    )
)

app.title = 'Example'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run_server(debug=True)