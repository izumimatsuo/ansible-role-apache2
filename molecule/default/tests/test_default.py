import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apache2_is_installed(host):
    package = host.package("httpd")
    assert package.is_installed
    assert package.version.startswith("2.4")


def test_apache2_running_and_enabled(host):
    service = host.service("httpd")
    assert service.is_running
    assert service.is_enabled


def test_apache2_is_listen(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
