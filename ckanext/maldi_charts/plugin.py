# encoding: utf-8 ##

import ckan.plugins as plugins


class ExampleIAuthFunctionsPlugin(plugins.SingletonPlugin):
    pass

'''import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MaldiChartsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'maldi_charts')
'''
