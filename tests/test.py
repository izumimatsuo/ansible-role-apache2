# -*- coding:utf8 -*-

def test_apache2_is_installed(host):
    apache2 = host.package("httpd")
    assert apache2.is_installed
    assert apache2.version.startswith("2.4")

def test_apache2_running_and_enabled(host):
    apache2 = host.service("httpd")
    assert apache2.is_running
    assert apache2.is_enabled

def test_apache2_is_listen(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
