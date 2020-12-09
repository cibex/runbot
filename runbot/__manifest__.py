# -*- coding: utf-8 -*-
{
    'name': "runbot",
    'summary': "Runbot",
    'description': "Runbot for Odoo 13.0",
    'author': "Odoo SA",
    'website': "http://runbot.odoo.com",
    'category': 'Website',
    'version': '5.1',
    'depends': ['base', 'base_automation', 'website'],
    'data': [
        'templates/dockerfile.xml',
        'data/dockerfile_data.xml',
        'data/build_parse.xml',
        'data/error_link.xml',
        'data/runbot_build_config_data.xml',
        'data/runbot_data.xml',
        'data/runbot_error_regex_data.xml',
        'data/website_data.xml',

        'security/runbot_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',

        'templates/badge.xml',
        'templates/batch.xml',
        'templates/branch.xml',
        'templates/build.xml',
        'templates/build_stats.xml',
        'templates/bundle.xml',
        'templates/commit.xml',
        'templates/dashboard.xml',
        'templates/frontend.xml',
        'templates/git.xml',
        'templates/nginx.xml',
        'templates/owl.xml',
        'templates/utils.xml',
        'templates/build_error.xml',

        'views/branch_views.xml',
        'views/build_error_views.xml',
        'views/build_views.xml',
        'views/bundle_views.xml',
        'views/commit_views.xml',
        'views/config_views.xml',
        'views/dockerfile_views.xml',
        'views/error_log_views.xml',
        'views/host_views.xml',
        'views/repo_views.xml',
        'views/res_config_settings_views.xml',
        'views/stat_views.xml',
        'views/upgrade.xml',
        'views/warning_views.xml',

        'wizards/mutli_build_wizard_views.xml',
        'wizards/stat_regex_wizard_views.xml',
    ],
    'license': 'LGPL-3',
}
