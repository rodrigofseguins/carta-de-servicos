import yaml
from flask import render_template

def load_config(file_name):
    """Carrega o arquivo YAML da pasta config."""
    with open(f'app/config/{file_name}', 'r', encoding="utf-8") as file:
        return yaml.safe_load(file)

def setup_routes(app):
    """Define as rotas da aplicação."""
    
    @app.route('/render/<template_name>/<config_file>')
    def render_from_template(template_name, config_file):
        """
        Rota para renderizar um template com dados de um arquivo YAML.
        :param template_name: Nome do template HTML.
        :param config_file: Nome do arquivo YAML.
        """
        config = load_config(config_file)
        return render_template(template_name, **config)
